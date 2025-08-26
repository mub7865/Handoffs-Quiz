import streamlit as st  # type: ignore
import random
import time

st.title("Quiz Application")

quiz_questions = [
    {
        "question": "What is the primary purpose of a Handoff in the OpenAI Agents SDK?",
        "options": ["To terminate the agent loop", "To delegate tasks from one agent to another for specialized processing", "To reset model settings", "To stream partial outputs"],
        "answer": "To delegate tasks from one agent to another for specialized processing"
    },
    {
        "question": "How is a Handoff implemented in the SDK?",
        "options": ["As a specialized tool call that transfers control to another agent", "By cloning the current agent", "Through direct API calls", "By resetting the context"],
        "answer": "As a specialized tool call that transfers control to another agent"
    },
    {
        "question": "Which parameter is used to configure Handoffs in an Agent's constructor?",
        "options": ["tools=[agent1, agent2]", "handoffs=[agent1, agent2]", "guardrails=[agent1, agent2]", "model_settings=handoff"],
        "answer": "handoffs=[agent1, agent2]"
    },
    {
        "question": "In the following code, what triggers a Handoff? ```python\nfrom agents import Agent\ntriage = Agent(name='Triage', instructions='Handoff based on language', handoffs=[spanish_agent, english_agent])\n```",
        "options": ["Manual call to handoff()", "LLM decides based on instructions during the agent loop", "When max_turns is reached", "Only if guardrails fail"],
        "answer": "LLM decides based on instructions during the agent loop"
    },
    {
        "question": "What happens to the agent loop when a Handoff is executed?",
        "options": ["The loop pauses and a new loop starts in the target agent", "The loop terminates immediately", "Both agents run in parallel", "The context is discarded"],
        "answer": "The loop pauses and a new loop starts in the target agent"
    },
    {
        "question": "What is the role of the `input_type` parameter in Handoff configuration?",
        "options": ["To specify the data type expected by the target agent", "To set the output format", "To limit tool calls", "To enable streaming"],
        "answer": "To specify the data type expected by the target agent"
    },
    {
        "question": "How does `input_filter` function in a Handoff?",
        "options": ["It validates or transforms input before passing to the target agent", "It filters output types", "It restricts handoff frequency", "It disables guardrails"],
        "answer": "It validates or transforms input before passing to the target agent"
    },
    {
        "question": "What does the `is_enabled` parameter control in a Handoff?",
        "options": ["Whether the handoff functionality is active for the agent", "If tools are enabled", "The streaming mode", "The cloning behavior"],
        "answer": "Whether the handoff functionality is active for the agent"
    },
    {
        "question": "What is the purpose of the `on_handoff` parameter in Handoff configuration?",
        "options": ["To define a callback function executed when a handoff occurs", "To reset tool choices", "To set the max_turns limit", "To enable tracing"],
        "answer": "To define a callback function executed when a handoff occurs"
    },
    {
        "question": "What is the default behavior if `is_enabled` is set to False for a Handoff?",
        "options": ["The handoff is ignored, and the agent continues its loop", "The agent raises an error", "The handoff executes anyway", "The context is reset"],
        "answer": "The handoff is ignored, and the agent continues its loop"
    },
    {
        "question": "In a multi-agent workflow with handoffs, how is the final output determined?",
        "options": ["The output comes from the last agent in the handoff chain", "All agents combine their outputs", "Only the first agent’s output is used", "The Runner decides randomly"],
        "answer": "The output comes from the last agent in the handoff chain"
    },
    {
        "question": "Consider this code: ```python\nagent1 = Agent(name='A1', handoffs=[agent2])\nresult = Runner.run_sync(agent1, 'Task')\n``` If agent1 hands off to agent2, what happens to agent1’s loop?",
        "options": ["Agent1’s loop terminates, and agent2’s loop takes over", "Both loops run concurrently", "Agent1 retries the task", "An error is raised"],
        "answer": "Agent1’s loop terminates, and agent2’s loop takes over"
    },
    {
        "question": "How does the SDK ensure context continuity during a Handoff?",
        "options": ["Context is automatically passed to the target agent via sessions", "Context is reset for each handoff", "Context is not supported in handoffs", "Manual context transfer is required"],
        "answer": "Context is automatically passed to the target agent via sessions"
    },
    {
        "question": "What is a practical use case for Handoffs in the SDK?",
        "options": ["To split tasks between agents with specialized instructions, like language-specific processing", "To duplicate agent configurations", "To limit tool usage", "To enforce output types"],
        "answer": "To split tasks between agents with specialized instructions, like language-specific processing"
    },
    {
        "question": "In a Handoff, what happens if the target agent lacks the required `input_type`?",
        "options": ["The handoff fails with a validation error", "The input is ignored", "The agent clones itself", "The loop retries automatically"],
        "answer": "The handoff fails with a validation error"
    },
    {
        "question": "How can `input_filter` be used in a Handoff?",
        "options": ["To preprocess or validate input data before the target agent processes it", "To filter the final output", "To set temperature settings", "To enable parallel tool calls"],
        "answer": "To preprocess or validate input data before the target agent processes it"
    },
    {
        "question": "What is the effect of setting `on_handoff` to a custom function?",
        "options": ["It executes custom logic, like logging or preprocessing, when the handoff occurs", "It overrides the target agent’s instructions", "It disables the handoff", "It resets the context"],
        "answer": "It executes custom logic, like logging or preprocessing, when the handoff occurs"
    },
    {
        "question": "In a Handoff chain, what limits the number of handoffs?",
        "options": ["The max_turns parameter in the Runner", "The number of tools", "The API key limit", "The output_type setting"],
        "answer": "The max_turns parameter in the Runner"
    },
    {
        "question": "Can a single agent have multiple handoff targets?",
        "options": ["Yes, specified as a list in handoffs=[agent1, agent2, ...]", "No, only one handoff target is allowed", "Only if tools are disabled", "Only with parallel_tool_calls enabled"],
        "answer": "Yes, specified as a list in handoffs=[agent1, agent2, ...]"
    },
    {
        "question": "What happens if a Handoff is attempted but no target agent is configured?",
        "options": ["The agent loop continues without handoff", "An error is raised", "The agent clones itself", "The output is streamed"],
        "answer": "The agent loop continues without handoff"
    },
    {
        "question": "In the SDK, how does the LLM decide which agent to hand off to?",
        "options": ["Based on the instructions and context provided to the agent", "Randomly from the handoffs list", "Based on tool_choice settings", "Using guardrails only"],
        "answer": "Based on the instructions and context provided to the agent"
    },
    {
        "question": "What is the relationship between Handoffs and the agent loop?",
        "options": ["Handoffs are special tool calls that pause the current loop and start a new one in the target agent", "Handoffs run in parallel with the loop", "Handoffs terminate the loop permanently", "Handoffs are unrelated to the loop"],
        "answer": "Handoffs are special tool calls that pause the current loop and start a new one in the target agent"
    },
    {
        "question": "How does `is_enabled` interact with guardrails during a Handoff?",
        "options": ["If is_enabled=False, guardrails are bypassed for the handoff", "Guardrails are always applied, regardless of is_enabled", "is_enabled controls guardrail execution", "Guardrails are not applicable to handoffs"],
        "answer": "Guardrails are always applied, regardless of is_enabled"
    },
    {
        "question": "In a Handoff scenario, what is the role of Pydantic models?",
        "options": ["To validate input_type for the target agent", "To generate tools automatically", "To set model settings", "To handle tracing"],
        "answer": "To validate input_type for the target agent"
    },
    {
        "question": "Consider this code: ```python\nagent1 = Agent(name='A1', handoffs=[agent2], instructions='Handoff if complex')\n``` What triggers the handoff to agent2?",
        "options": ["The LLM’s interpretation of ‘complex’ in the instructions", "A manual call to handoff()", "The max_turns limit", "An output_type mismatch"],
        "answer": "The LLM’s interpretation of ‘complex’ in the instructions"
    },
    {
        "question": "What is a key benefit of using Handoffs in multi-agent workflows?",
        "options": ["Enables modular task delegation for scalability and specialization", "Reduces the need for instructions", "Eliminates context management", "Disables tool usage"],
        "answer": "Enables modular task delegation for scalability and specialization"
    },
    {
        "question": "How does a Handoff differ from a regular tool call?",
        "options": ["A handoff transfers control to another agent, while a tool call executes a function and returns results", "Handoffs are only for streaming", "Tool calls terminate the loop", "There is no difference"],
        "answer": "A handoff transfers control to another agent, while a tool call executes a function and returns results"
    },
    {
        "question": "What happens to tracing during a Handoff?",
        "options": ["Tracing continues, capturing the handoff and target agent’s execution", "Tracing stops at the handoff", "Tracing is disabled for handoffs", "Tracing requires manual configuration"],
        "answer": "Tracing continues, capturing the handoff and target agent’s execution"
    },
    {
        "question": "In a Handoff, what ensures the target agent receives the correct input?",
        "options": ["input_type and input_filter validate and preprocess the input", "The Runner automatically formats the input", "The context is ignored", "The output_type of the source agent"],
        "answer": "input_type and input_filter validate and preprocess the input"
    },
    {
        "question": "What is the maximum depth of a Handoff chain controlled by?",
        "options": ["The max_turns setting in the Runner", "The number of agents in the handoffs list", "The tool_choice setting", "The temperature parameter"],
        "answer": "The max_turns setting in the Runner"
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
