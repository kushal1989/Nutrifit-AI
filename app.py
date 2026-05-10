from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------- LOAD ENV ---------------- #
load_dotenv()

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="NutriFit AI",
    page_icon="🥗",
    layout="centered"
)

st.markdown(
    """
    <style>

    .stApp {
        background-image: url("https://images.unsplash.com/photo-1490645935967-10de6ba17061");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .main {
        background: rgba(0,0,0,0.5);
        padding: 20px;
        border-radius: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
.stTextInput > div > div > input {
    font-size: 18px;
    padding: 12px;
    border-radius: 10px;
}


.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #4CAF50;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown(
    "<div class='main-title'>🥗 NutriFit AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Smart Nutrition & Fitness Guidance Assistant</div>",
    unsafe_allow_html=True
)

# ---------------- EXAMPLES ---------------- #
with st.expander("💡 Example Questions"):
    st.write("""
    • How many calories are in 2 bananas?  
    • Suggest a high protein Indian breakfast  
    • How can I lose belly fat naturally?  
    • Best foods for muscle gain  
    • Give me a healthy diet plan  
    • Is pizza healthy for dinner?  
    • Suggest workouts for beginners  
    """)

# ---------------- PROMPT TEMPLATE ---------------- #
template = """
You are NutriFit AI, an expert Nutritionist and Fitness Trainer
with 15+ years of experience.

Answer the user's nutrition and fitness-related questions
in a professional, beginner-friendly, and motivating way.

Instructions:
- Give practical health advice.
- Suggest healthy food alternatives if relevant.
- Mention calorie or nutrition information if needed.
- Recommend workouts or healthy habits when appropriate.
- Use proper headings and bullet points.
- Keep the tone supportive and encouraging.
- If the query is unrelated to nutrition, fitness, food,
  calories, workout, or health, politely say:
  "Sorry, I can only assist with fitness, nutrition,
   calories, food, and healthy lifestyle-related queries."

Question:
{query}
"""

# ---------------- PROMPT ---------------- #
prompt = ChatPromptTemplate.from_template(template)

# ---------------- MODEL ---------------- #
model = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

with st.sidebar:

    st.title("🥗 NutriFit AI")

    st.markdown("---")

    st.subheader("💡 What You Can Ask")

    st.write("""
    • Calorie related questions  
    • Weight loss tips  
    • Healthy diet plans  
    • Muscle gain suggestions  
    • Workout recommendations  
    • Healthy food alternatives  
    """)

    st.markdown("---")

    st.subheader("🔥 Popular Queries")

    st.write("""
    • High protein breakfast  
    • Foods for fat loss  
    • Healthy snacks  
    • Daily calorie intake  
    """)


# ---------------- CHAIN ---------------- #
chain = prompt | model

# ---------------- CHAT INPUT ---------------- #
user_input = st.text_input(
    "Ask anything about fitness, food, calories, or healthy lifestyle:",
    placeholder="Example: Suggest a healthy breakfast for weight loss"
)

# ---------------- BUTTON ---------------- #
if st.button("Generate Response"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Analyzing your health query..."):

            response = chain.invoke({
                "query": user_input
            })

        st.write(response)
