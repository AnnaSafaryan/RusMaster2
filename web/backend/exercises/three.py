"""
Порядок слов
    В предложении из исходного текста перемешаны слова, и нужно расставить их так,
    чтобы получить предложение, правильное с точки зрения грамматики и смысла.
    Вариантов может быть несколько, в качестве примера в ответе
    предложен вариант из исходного текста.
"""

# def main(preprocessed_text):
#     pass


if __name__ == "__main__":
    from web.backend.config import config
    from web.backend.helpers.preprocessing import get_preprocessed
    from web.backend.helpers.utils import create_path, generate_id

    def main(file_path):
        file_id = generate_id(file_path)
        temp_path = config.TEMP_DIR / f"{file_id}"
        preprocessed_path = temp_path / config.PREPROCESSED_NAME
        create_path(temp_path)
        preprocessed = get_preprocessed(preprocessed_path)
        return preprocessed

    file_path = config.TEST_TEXT_PATH
    preprocessed = main(file_path)
    main(preprocessed)
