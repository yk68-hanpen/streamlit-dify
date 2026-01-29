import streamlit as st
import requests
import time

# --- 1. Dify呼び出し関数の定義 (ここが抜けていました) ---
def call_dify(user_input):
    # DifyのAPIエンドポイント
    url = "https://api.dify.ai/v1/chat-messages"
    
    headers = {
        "Authorization": f"Bearer {st.secrets['DIFY_API_KEY']}",
        "Content-Type": "application/json"
    }
    
    data = {
        "inputs": {},
        "query": user_input,
        "response_mode": "blocking",
        "user": "testuser"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        # Difyからの回答テキストを返す
        return result.get("answer", "解析結果が得られませんでした。")
    except Exception as e:
        return f"通信エラーが発生しました: {str(e)}"

# --- 2. 認証ロジック ---
def check_password():
    def login_form():
        with st.form("login"):
            st.subheader("ログイン")
            user = st.text_input("Username")
            pw = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
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

# --- 3. メインUI ---
if check_password():
    st.title("🛒 商品レビュー判定AI (Dify稼働中)")
    
    # ログアウトボタンをサイドバーに配置
    if st.sidebar.button("ログアウト"):
        st.session_state["logged_in"] = False
        st.rerun()

    review_text = st.text_area("レビュー内容をペーストしてください", height=200)
    
    if st.button("AI判定を実行"):
        if not review_text.strip():
            st.warning("テキストを入力してください。")
        else:
            with st.spinner("Dify API 通信中..."):
                # ここで上で定義した call_dify を呼び出します
                answer = call_dify(review_text)
                st.markdown("---")
                st.markdown("### 🤖 AIの回答")
                st.write(answer)