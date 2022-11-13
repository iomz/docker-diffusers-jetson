FROM nvcr.io/nvidia/l4t-pytorch:r35.1.0-pth1.11-py3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN set -eux; \
    apt-get update && apt-get install -y \
       python3 python3-pip \
    ; \
    rm -rf /var/lib/apt/lists/*

RUN /bin/bash -c "pip install --upgrade diffusers[torch]"
RUN pip install --upgrade diffusers transformers scipy numpy==1.23.4 protobuf
RUN pip install accelerate ftfy

WORKDIR /app

ENTRYPOINT ["python3", "/app/txt2img.py"]
CMD ["a photograph of an astronaut riding a horse"]
