
# ------Required a lot of RAM, CPU, GPU----------------

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    ),
)

model = ChatHuggingFace(llm=llm, verbose=True)
response = model.invoke("what is capital of India")
print(response.content)