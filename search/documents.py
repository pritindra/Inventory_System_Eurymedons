from django_elasticsearch_dsl import Document, Index
from interface.models import Arsenal

arsenals = Index('arsenals')

@arsenals.doc_type
class ArsenalDocument(Document):
    class Django:
        model = Arsenal

        fields = [
            'arsenal_name',
            'arsenal_type'
        ]
