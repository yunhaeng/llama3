# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed in accordance with the terms of the Llama 3 Community License Agreement.

#llama3 패키지 구성을 위해 setuptools 라이브러리를 활용.
from setuptools import find_packages, setup

#requirements.txt 내의 필수 패키지를 리스트 형식으로 리턴하는 함수.
def get_requirements(path: str):
    return [l.strip() for l in open(path)]

#setup 함수로 llama3 패키지를 생성.
setup(
    name="llama3",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
