import streamlit as st
from src import single_stock, sip
import io

MAGE_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/259/mage_1f9d9.png"
# Set page title and favicon.
st.set_page_config(
    page_title="Simplified Stock Analyzer", page_icon=MAGE_EMOJI_URL, layout="wide"
)


def main():
    # Render the readme as markdown using st.markdown.
    readme_file = io.open("README.md", mode="r", encoding="utf-8")
    readme_text = st.markdown(readme_file.read())

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("想怎麼查詢呢？")
    selector = ["說明", "單一投資標的查詢", "定期定額查詢"]
    app_mode = st.sidebar.selectbox("選擇分析模式",
                                    selector)

    if app_mode == selector[0]:
        st.sidebar.success('請選擇其他模式以繼續執行 😊')
    elif app_mode == selector[1]:
        readme_text.empty()
        st.sidebar.info('目前僅有此模式資源「與大盤比較」的功能。')
        single_stock.main()
    elif app_mode == selector[2]:
        readme_text.empty()
        st.sidebar.info('股數不為整數。數值僅作為參考。')
        sip.main()


@st.cache()
def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/streamlit/demo-self-driving/master/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")


if __name__ == '__main__':
    main()
