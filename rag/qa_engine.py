# from llama_cpp import Llama

# # Load your local GGUF model
# # llm = Llama(model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)
# llm = Llama(
#     model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
#     n_ctx=2048,
#     n_threads=8,         # Use available CPU cores
#     n_gpu_layers=32,     # If you have GPU via cuBLAS/Metal
#     temperature=0.3,     # More deterministic
#     top_p=0.9,
#     top_k=40,
#     repeat_penalty=1.1   # Prevents repeating phrases
# )

# def generate_answer(context: str, question: str) -> str:
#     prompt = f"""
# You are a helpful assistant. Use the context below to answer the question.

# Context:
# {context}

# Question:
# {question}

# Answer:
# """
#     output = llm(prompt, stop=["\n\n", "User:"], echo=False)
#     return output["choices"][0]["text"].strip()


# from llama_cpp import Llama

# # Load your local GGUF model with performance-tuned settings
# llm = Llama(
#     model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
#     n_ctx=2048,
#     n_threads=8,         # Match to your CPU core count
#     n_gpu_layers=32,     # Optimize based on GPU availability
#     temperature=0.3,     # Lower temp = more deterministic answers
#     top_p=0.9,
#     top_k=40,
#     repeat_penalty=1.1
# )

# # Improved answer generation with better prompting
# def generate_answer(context: str, question: str) -> str:
#     prompt = f"""You are a knowledgeable assistant helping a user understand a transcript of a YouTube video.

# Use only the context below to answer the question truthfully. 
# If the answer is not clearly present, say: "I'm not sure based on the transcript."

# ---
# Context:
# \"\"\"{context}\"\"\"

# Question:
# {question}

# Answer:"""

#     output = llm(prompt, stop=["\n\n", "User:", "Question:"], echo=False, max_tokens=1024)
#     return output["choices"][0]["text"].strip()








from llama_cpp import Llama

# Cache the loaded LLM instance per model path
_loaded_models = {}

def get_llm(model_path: str, temperature: float):
    key = (model_path, temperature)
    if key not in _loaded_models:
        print(f"🚀 Loading LLM from {model_path} (temp={temperature})...")
        _loaded_models[key] = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=8,
            n_gpu_layers=32,
            temperature=temperature,
            top_p=0.9,
            top_k=40,
            repeat_penalty=1.1,
        )
    return _loaded_models[key]


def generate_answer(context: str, question: str, model_path: str, temperature: float = 0.3) -> str:
    llm = get_llm(model_path, temperature)

    prompt = f"""You are a knowledgeable assistant helping a user understand a transcript of a YouTube video.

Use only the context below to answer the question truthfully. 
If the answer is not clearly present, say: "I'm not sure based on the transcript."

---
Context:
\"\"\"{context}\"\"\"

Question:
{question}

Answer:"""

    output = llm(prompt, stop=["\n\n", "User:", "Question:"], echo=False, max_tokens=1024)
    return output["choices"][0]["text"].strip()
