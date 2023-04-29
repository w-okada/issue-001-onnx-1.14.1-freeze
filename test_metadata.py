import onnxruntime


if __name__ == "__main__":
    print("load start")
    onnx_session = onnxruntime.InferenceSession(
        "metadata.onnx",
        providers=[
            "CPUExecutionProvider",
        ],
    )
    print("load end")
