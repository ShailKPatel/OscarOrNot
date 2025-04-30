import streamlit as st

# Logo
image = "resources/logo.png"
st.logo(image, size='large')

with st.container():
    """ # 🏆 OscarOrNot 🎬
    A deep learning-powered tool to predict whether a film has what it takes to win the Best Picture Oscar — based on box office, critical acclaim, and cinematic pedigree.

    ## 🔍 Overview   
    OscarOrNot evaluates the Oscar-worthiness of films using a neural network trained on historical movie data. By analyzing metadata like release timing, genre, critical reception, and past awards, the model surfaces patterns common to Oscar-winning films. It's a data-driven lens into Hollywood’s most elite contest.

    ## ✨ Key Features
    ✔ Oscar-Win Probability Prediction: Binary classifier trained on historical Best Picture data.  
    ✔ Strategic Timing Features: Release month, Oscar proximity, seasonal patterns.  
    ✔ Prestige Metrics: Director/writer/actor Oscar nominations and wins.  
    ✔ Critical & Commercial Indicators: Rotten Tomatoes, IMDb, Google Trends, box office stats.  
    ✔ Neural Network Architecture: Built in TensorFlow/Keras, fine-tuned for accuracy and recall.  
    ✔ Visual Model Analysis: ROC curves, feature importances, AUC scores, confusion matrix.  
    ✔ Tech Stack: Python, Pandas, NumPy, TensorFlow, Streamlit.  
    
    
    ## 🎬 Explore the Tool
    """

with st.container(border=True):
    "# 🎥 Try the Prediction Model"
    "###### Test the OscarOrNot model using metadata from any movie. You can try a real title or experiment with custom inputs."
    st.page_link("page_files/Try_Model.py", label="Try Prediction", icon="🧠")

with st.container(border=True):
    "# 📊 View Model Insights"
    "###### Dive into the model’s performance — explore evaluation metrics, error cases, and how each feature impacts predictions."
    st.page_link("page_files/View_Model_Analysis.py", label="Model Analysis", icon="📈")  

with st.container(border=True):
    "# 💬 Got Feedback?"
    "###### We'd love to hear your thoughts on the tool. Whether it’s bugs, feature requests, or praise — we’re listening."
    st.page_link("page_files/Feedback.py", label="Give Feedback", icon="💭")    

with st.container(border=True):
    "# 👨‍🔬 Learn More"
    "###### Curious about the dataset, modeling decisions, or contributors? Check out the credits page."
    st.page_link("page_files/Credits.py", label="Credits", icon="📇")

with st.container(border=True):
    "# 🌍 TO Another Universe..."
    "#### 🎓 Attend2Achieve – Cracking Academic Patterns"
    st.write(
        "*Attend2Achieve* explores academic fairness and performance trends using student attendance and grade correlations. "
        "From skewness to standard deviation, it visualizes learning dynamics and helps educators diagnose problems early. "
        "If you’re into data-driven insight outside the film industry, this might interest you too."
    )

    st.page_link("https://attend2achieve.streamlit.app", label="Try Attend2Achieve", icon="🚀", use_container_width=True)
