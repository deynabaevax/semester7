import streamlit as st
import multipages
import classify
import similar
import home

# Initiate the app
application = multipages.MultiApp()

# Adding all pages here
application.add_app("Home", home.homepage)
application.add_app("Classify", classify.classify)
application.add_app("Get Similar Episodes", similar.recommend_episodes)


# Run the main app
application.run()
