#!/usr/bin/env bash
set -euo pipefail

APP_DIR="genai_scaffolding_pro"
BUILD_DIR="build/lambda"
ZIP_NAME="genai_scaffolding_lambda.zip"

rm -rf "${BUILD_DIR}"
mkdir -p "${BUILD_DIR}"
pip install -r requirements.txt -t "${BUILD_DIR}"
cp -R ${APP_DIR} "${BUILD_DIR}/${APP_DIR}"
cd "${BUILD_DIR}"
zip -r "${ZIP_NAME}" .
echo "Lambda package at: ${BUILD_DIR}/${ZIP_NAME}"