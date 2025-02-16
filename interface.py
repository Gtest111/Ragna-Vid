import gradio as gr
from ytbot import *

with gr.Blocks() as interface:

    gr.Markdown(
        "<h2 style='text-align: center;'>📽️ YouTube Video Summarizer & Q&A 🤖</h2>"
    )

    gr.Markdown(
        "<p style='text-align: center; font-size: 16px;'>🔍 Get a quick summary of any YouTube video and ask questions about its content!</p>"
    )

    # Input field for YouTube URL
    video_url = gr.Textbox(label="🔗 YouTube Video URL", placeholder="Paste the YouTube video link here 🎥")

    # Outputs for summary and answer
    summary_output = gr.Textbox(label="📜 Video Summary", lines=5, interactive=False)
    question_input = gr.Textbox(label="❓ Ask a Question About the Video", placeholder="Type your question here... 🤔")
    answer_output = gr.Textbox(label="💡 Answer to Your Question", lines=5, interactive=False)

    # Buttons for selecting functionalities after fetching transcript
    summarize_btn = gr.Button("✨ Summarize Video")
    question_btn = gr.Button("🔍 Ask a Question")

    # Display status message for transcript fetch
    transcript_status = gr.Textbox(label="📢 Transcript Status", interactive=False)

    # Set up button actions
    summarize_btn.click(summarize_video, inputs=video_url, outputs=summary_output)
    question_btn.click(answer_question, inputs=[video_url, question_input], outputs=answer_output)

# Launch the app with specified server name and port
interface.launch(server_name="0.0.0.0", server_port=7860)
