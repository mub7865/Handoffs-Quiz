import streamlit as st  # type: ignore
import random
import time

st.title("Quiz Application")

quiz_questions = [
    {
        "question": "What is the primary definition of an Agent in the OpenAI Agents SDK?",
        "options": ["A database connector for AI tasks", "An LLM equipped with instructions, tools, handoffs, and guardrails", "A streaming service for real-time data", "A compiler for Python code"],
        "answer": "An LLM equipped with instructions, tools, handoffs, and guardrails"
    },
    {
        "question": "In the OpenAI Agents SDK, what role does an Agent play in the overall primitives?",
        "options": ["It handles only guardrail validations", "It acts as the core LLM component for executing tasks in the agent loop", "It manages external API keys exclusively", "It compiles handoffs into binaries"],
        "answer": "It acts as the core LLM component for executing tasks in the agent loop"
    },
    {
        "question": "How is a basic Agent created in the SDK, as shown in the hello world example?",
        "options": ["Agent.create(name='Assistant', instructions='You are helpful')", "Agent(name='Assistant', instructions='You are a helpful assistant')", "new Agent('Assistant', 'You are helpful')", "Agent.init(name='Assistant')"],
        "answer": "Agent(name='Assistant', instructions='You are a helpful assistant')"
    },
    {
        "question": "What is the purpose of the 'name' parameter in Agent configuration?",
        "options": ["To set the LLM model version", "To provide a unique identifier for tracing, logging, and debugging", "To define the output type", "To override tool descriptions"],
        "answer": "To provide a unique identifier for tracing, logging, and debugging"
    },
    {
        "question": "In Agent configuration, what does the 'instructions' parameter represent?",
        "options": ["A list of tools to equip the agent", "A string or callable that guides the LLM's behavior and task execution", "The maximum number of turns in the loop", "The API key for authentication"],
        "answer": "A string or callable that guides the LLM's behavior and task execution"
    },
    {
        "question": "What are Dynamic Instructions in the context of Agent configuration?",
        "options": ["Fixed strings that cannot change during runtime", "Instructions that can be a callable function, dynamically generating prompts based on context each time the agent runs", "Instructions limited to Markdown syntax", "Automatic cloning of instructions for parallel agents"],
        "answer": "Instructions that can be a callable function, dynamically generating prompts based on context each time the agent runs"
    },
    {
        "question": "If the 'instructions' in an Agent is a callable, when is it invoked?",
        "options": ["Only at Agent creation", "During each iteration of the agent loop to allow context-aware prompting", "After handoff completion", "When tracing is enabled"],
        "answer": "During each iteration of the agent loop to allow context-aware prompting"
    },
    {
        "question": "What happens if Dynamic Instructions raise an error during execution?",
        "options": ["The agent loop terminates immediately", "The error is caught and the agent falls back to default instructions", "It may disrupt the agent loop, requiring proper error handling in the callable", "The SDK automatically retries up to 3 times"],
        "answer": "It may disrupt the agent loop, requiring proper error handling in the callable"
    },
    {
        "question": "In Agent configuration, what is the 'output_type' parameter used for?",
        "options": ["To specify the input format for tools", "To enforce a Pydantic model for structured final output, looping until matched", "To set the streaming mode", "To define handoff targets"],
        "answer": "To enforce a Pydantic model for structured final output, looping until matched"
    },
    {
        "question": "If 'output_type' is not specified in an Agent, what is the default behavior?",
        "options": ["The agent raises an error", "The first LLM response without tool calls or handoffs is taken as the final output", "It defaults to string output with Markdown", "It clones the agent for retry"],
        "answer": "The first LLM response without tool calls or handoffs is taken as the final output"
    },
    {
        "question": "What is Cloning in the context of an Agent?",
        "options": ["Duplicating tools for parallel calls", "Creating a copy of the Agent with the same configuration for independent or parallel workflows", "Merging two agents into one", "Resetting the agent's context"],
        "answer": "Creating a copy of the Agent with the same configuration for independent or parallel workflows"
    },
    {
        "question": "How might you clone an Agent in the SDK?",
        "options": ["agent.clone()", "Agent.copy(agent)", "By re-instantiating with the same parameters", "Cloning is not supported; agents are immutable"],
        "answer": "agent.clone()"
    },
    {
        "question": "In Agent configuration, where are Model Settings like temperature applied?",
        "options": ["Directly in the Runner class only", "As optional parameters in the Agent constructor or during LLM calls in the loop", "In tool decorators exclusively", "They are fixed and cannot be configured"],
        "answer": "As optional parameters in the Agent constructor or during LLM calls in the loop"
    },
    {
        "question": "What does the 'temperature' model setting control in an Agent?",
        "options": ["The speed of execution", "The randomness and creativity of the LLM's responses (higher values increase diversity)", "The number of parallel tool calls", "The frequency of handoffs"],
        "answer": "The randomness and creativity of the LLM's responses (higher values increase diversity)"
    },
    {
        "question": "In Model Settings for an Agent, what is the default value for 'top_p'?",
        "options": ["0.0", "1.0", "0.5", "None"],
        "answer": "1.0"
    },
    {
        "question": "What does 'top_k' in Agent Model Settings refer to?",
        "options": ["Limiting sampling to the top K most likely tokens", "The maximum turns in the agent loop", "The number of guardrails", "The depth of cloning"],
        "answer": "Limiting sampling to the top K most likely tokens"
    },
    {
        "question": "How does 'frequency_penalty' affect an Agent's LLM output?",
        "options": ["It penalizes new tokens based on their frequency in the text so far, reducing repetition", "It increases the likelihood of frequent words", "It controls tool call frequency", "It penalties failed handoffs"],
        "answer": "It penalizes new tokens based on their frequency in the text so far, reducing repetition"
    },
    {
        "question": "What is the role of 'presence_penalty' in Agent configuration?",
        "options": ["It penalizes tokens based on whether they appear in the text at all, encouraging new topics", "It resets tool choices", "It enables dynamic instructions", "It limits output types"],
        "answer": "It penalizes tokens based on whether they appear in the text at all, encouraging new topics"
    },
    {
        "question": "In Agent Model Settings, what does 'tool_choice' control?",
        "options": ["Whether and how the LLM decides to call tools ('auto', 'required', 'none', etc.)", "The choice of output type", "The selection of handoff targets", "The cloning method"],
        "answer": "Whether and how the LLM decides to call tools ('auto', 'required', 'none', etc.)"
    },
    {
        "question": "What is 'parallel_tool_calls' in Agent configuration?",
        "options": ["A boolean to enable or disable simultaneous execution of multiple tool calls", "A setting for parallel agent cloning", "A limit on handoff parallelism", "A guardrail for output parallelism"],
        "answer": "A boolean to enable or disable simultaneous execution of multiple tool calls"
    },
    {
        "question": "In Agent configuration, what does 'tool_use_behaviour' define?",
        "options": ["The strategy for tool usage, such as 'default', 'always', or 'selective' based on context", "The behavior of dynamic instructions", "The reset mechanism for tools", "The tracing level for tools"],
        "answer": "The strategy for tool usage, such as 'default', 'always', or 'selective' based on context"
    },
    {
        "question": "What is the purpose of 'reset_tool_choice' in an Agent?",
        "options": ["A method to reset the tool_choice setting mid-run for adaptive behavior", "To reset the entire agent configuration", "To clone tools", "To change output types dynamically"],
        "answer": "A method to reset the tool_choice setting mid-run for adaptive behavior"
    },
    {
        "question": "When might 'reset_tool_choice' be called in an Agent?",
        "options": ["After a handoff to restore default tool selection", "During cloning to duplicate choices", "In the agent loop to adjust based on previous responses", "It cannot be called; it's automatic"],
        "answer": "In the agent loop to adjust based on previous responses"
    },
    {
        "question": "In Agent configuration, how are tools added?",
        "options": ["As a list in the constructor: tools=[tool1, tool2]", "By calling agent.add_tool()", "Tools are auto-detected", "Only through handoffs"],
        "answer": "As a list in the constructor: tools=[tool1, tool2]"
    },
    {
        "question": "What configuration option allows adding handoffs to an Agent?",
        "options": ["handoffs=[agent1, agent2] in the constructor", "By setting handoff=True", "Through model settings", "Handoffs are not configurable"],
        "answer": "handoffs=[agent1, agent2] in the constructor"
    },
    {
        "question": "How can guardrails be configured in an Agent?",
        "options": ["As a list of validation functions in the constructor: guardrails=[guard1, guard2]", "By enabling guardrails in Runner", "Guardrails are built-in and non-configurable", "Only for tools"],
        "answer": "As a list of validation functions in the constructor: guardrails=[guard1, guard2]"
    },
    {
        "question": "In the context of Agent configuration, what LLM model is typically used by default?",
        "options": ["gpt-3.5-turbo", "gpt-4o", "text-davinci-003", "No default; must be specified"],
        "answer": "gpt-4o"
    },
    {
        "question": "What environment variable is required for Agent configuration to function?",
        "options": ["OPENAI_API_KEY", "AGENT_NAME", "TOOL_PATH", "HANDOFF_ID"],
        "answer": "OPENAI_API_KEY"
    },
    {
        "question": "If an Agent is configured without tools, what happens in the agent loop?",
        "options": ["It raises an error", "The agent relies solely on instructions and LLM generation", "It automatically adds default tools", "It delegates to handoffs immediately"],
        "answer": "The agent relies solely on instructions and LLM generation"
    },
    {
        "question": "In advanced Agent configuration, how do model settings interact with the agent loop?",
        "options": ["They are applied during each LLM call in the loop for consistent behavior", "Only once at startup", "They are ignored in loops", "Only for tool calls"],
        "answer": "They are applied during each LLM call in the loop for consistent behavior"
    }
]

# Initialize session states
if "username" not in st.session_state:
    st.session_state.username = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

# Ask for user name before starting the quiz
if not st.session_state.quiz_started:
    st.session_state.username = st.text_input("Enter your name to start the quiz")
    if st.button("Start Quiz") and st.session_state.username.strip() != "":
        random.shuffle(quiz_questions)
        st.session_state.quiz_started = True
        st.success(f"Welcome {st.session_state.username}! Let's start the quiz 🎉")
    st.stop()

# Get current question
if st.session_state.question_index < len(quiz_questions):
    question = quiz_questions[st.session_state.question_index]
    st.subheader(f"Q{st.session_state.question_index + 1}: {question['question']}")
    selected_option = st.radio("Choose Your Answer", question["options"], key=f"q{st.session_state.question_index}")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect! The correct answer was: {question['answer']}")
        time.sleep(1.5)
        st.session_state.question_index += 1
        st.experimental_rerun()

# Quiz completed
else:
    st.balloons()
    st.success(f"🎉 Quiz Completed! Well done, {st.session_state.username}!")
    st.write(f"✅ Your Score: **{st.session_state.score} / {len(quiz_questions)}**")
    st.write("Thanks for playing the quiz. You did a great job!")

    # Option to restart
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.quiz_started = False
        st.experimental_rerun()
