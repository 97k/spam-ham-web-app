#!/usr/bin/env python
import os
import sys
import pickle
from utils import text_process


def importPipelines():
    pipeline = pickle.load(open('text_clf_pipeline.pkl', 'rb'))
    pipeline_second = pickle.load(open('spam_clf_model_pipeline_final_second.pkl', 'rb'))
    return pipeline, pipeline_second


if __name__ == "__main__":

    pipeline, pipeline_seond = importPipelines()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "textclassifier.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
