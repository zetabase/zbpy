#!/bin/bash
python -m grpc_tools.protoc -I protocol/ --python_out=. --grpc_python_out=. protocol/zbprotocol.proto