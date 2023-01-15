import streamlit as st
from PIL import Image


def homepage():
    image = Image.open('../images/logo-panda.png')
    st.image(image, width=200)
    st.title('AlgoShow')
    st.markdown('Engineers: Deyna Baeva, Akshara Shukla')

    st.markdown('')

    st.markdown(" Do you want to discover your next favorite tv show personally curated for you, reducing the search time? AlgoShow will cut down the scrolling time by 80% and suggest your top episodes just by a piece of text.")
    st.markdown('')
    st.markdown('')
    st.markdown('')

    with st.expander(label='Click here, to find out our methodology.'):
        st.write("""
                    Is AlgoShow Safe? Is it Legal to use AlgoShow?

                    Jazeker! AlgoShow doesn't require your name, your email, and your credit card number as we don't ask for a signup. Therefore, you can stay completely anonymous.

                    Why AlgoShow should be your TV Show recommendation site? - Some good reviews about AlgoShow
                    1. Safety
                    Because finding TV show shouldn't be a stressful task. No signup or registration is needed to recommend TV shows on AlgoShow, so you can stay safe and sound without giving any information for hackers or unwanted parties to track you down. We don't save any information of the user.

                    2. Minimal UI design
                    AlgoShow should be as easy as Google to input your text and to navigate. If you already have a title in mind, simply enter the keywords in the search box at the top of the site. 

                    3. Inclusive content library
                    For the first release of the application, we use the top watched tv shows such as Friends, The Office, Modern Family, Breaking Bad, Games Of Thrones, Big Bang Theory and more!

                    4. Ads and popups
                    There are absolutely zero ads on our site. 

                    7. Great customer care
                    At AlgShow, we understand that your experience comes first. Therefore, we try our best to listen to our users. Should there be any issue, please feel free to send us a message. Or if you cannot find a movie or TV show of interest, we are also on all ear to get your request.  

                    """)
