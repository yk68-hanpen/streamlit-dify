import streamlit as st
import time
import requests

def check_password():
    """ユーザー名とパスワードをチェックし、OKならTrueを返す"""
    def login_form():
        with st.form("login"):
            st.subheader("ログイン")
            user = st.text_input("Username")
            pw = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                # Secretsから取得した値と比較（または直接書き換え）
                if user == st.secrets.get("USERNAME", "admin") and \
                   pw == st.secrets.get("PASSWORD", "aws-tam-demo"):
                    st.session_state["logged_in"] = True
                    st.rerun()
                else:
                    st.error("❌ ユーザー名またはパスワードが違います")

    if not st.session_state.get("logged_in", False):
        login_form()
        return False
    return True

# 認証チェック
# --- UI部分 (既存の認証ロジックの後に入れる) ---
if check_password(): # 前回のログインチェック
    st.title("🛒 商品レビュー判定AI (Dify稼働中)")
    
    review_text = st.text_area("レビュー内容をペーストしてください", height=200)
    
    if st.button("AI判定を実行", variant="primary"):
        if not review_text.strip():
            st.warning("テキストを入力してください。")
        else:
            with st.spinner("Dify API 通信中..."):
                answer = call_dify(review_text)
                st.markdown("---")
                st.markdown("### 🤖 AIの回答")
                st.write(answer)