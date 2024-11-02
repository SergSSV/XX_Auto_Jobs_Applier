# В этом файле задаются настройки приложения

"""
Если этот режим активирован - откликаемся на все вакансии без разбора,
иначе просим LLM подбирать только те вакансии, которые тебе подходят
по интересам или по стеку
"""
MONKEY_MODE = False

"""
Этот режим нужен для проверки качества генерации сопроводительных писем.
Если режим активирован - не откликаемся на вакансии, а только сохраняем сгенерированные
сопроводительные письма в файл data_folder/output/llm_api_calls.json
"""
DEBUG_MODE = False

"""
Если этот режим активирован - приложение будет использовать одно готовое сопроводительное письмо 
для всех вакансий вместо генерирации отдельного сопроводительного письма для каждой вакансии.
Текст готового сопроводительного письма можно найти в файле strings.py, переменная fixed_cover_letter
"""
FIXED_COVER_LETTER = False

"""
Уровень логирования
Возможные значения:
    - "DEBUG"
    - "INFO"
    - "WARNING"
    - "ERROR"
    - "CRITICAL"
"""
MINIMUM_LOG_LEVEL = "DEBUG"

# Максимальное число откликов за один запуск.
# Учтите, что для hh.ru есть ограничение на не более чем 200 откликов в день (https://feedback.hh.ru/knowledge-base/article/1618)
MAX_APPLIES_NUM = 200

# Минимальное время, затрачиваемое на один отклик на вакансию
MINIMUM_WAIT_TIME_SEC = 10

"""
Тип LLM
Возможные значения:
    - "openai"
    - "claude"
    - "ollama"
    - "gemini"
    - "huggingface"
"""
LLM_MODEL_TYPE = "openai" 

# Модель LLM
LLM_MODEL = "gpt-4o-mini"  

# Если True - подавать в каждую компанию не более чем одну вакансию
APPLY_ONCE_AT_COMPANY = True

# словарь для подсчета стоимости запроса к модели
PRICE_DICT = {
    "gpt-4o": {
        "price_per_input_token": 2.5e-6,
        "price_per_output_token": 1e-5,
        },
    "gpt-4o-mini": {
        "price_per_input_token": 1.5e-7,
        "price_per_output_token": 6e-7,
        },
    }