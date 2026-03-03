import pandas as pd
from io import BytesIO

from app.services.tabular.normalizer import normalize_tabular
from app.core.exceptions import EmptyFileError, InvalidFileError
from app.utils.file_utils import validate_file_not_empty

def process_csv(contents: bytes):
    validate_file_not_empty(contents)
    
    try:
        df = pd.read_csv(BytesIO(contents))

        df = normalize_tabular(df)

        records = df.to_dict(orient="records")
        return records
    except Exception as e:
        raise InvalidFileError(str(e))