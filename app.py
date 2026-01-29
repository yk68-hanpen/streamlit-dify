import streamlit as st
import time

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
if check_password():
    # --- ここからメインコンテンツ ---
    st.sidebar.write(f"Logged in as: {st.secrets.get('USERNAME', 'admin')}")
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    st.title("🛒 商品レビュー判定AI")
    st.info("デモ用：現在は固定メッセージを返します。")

    review_text = st.text_area("レビュー内容", placeholder="ここにレビューをペーストしてください")
    if st.button("判定を実行"):
        with st.spinner("AI解析中..."):
            time.sleep(1)
            # デモ用ロジック
            if "悪い" in review_text:
                st.error("判定：ネガティブ")
            else:
                st.success("判定：ポジティブ")