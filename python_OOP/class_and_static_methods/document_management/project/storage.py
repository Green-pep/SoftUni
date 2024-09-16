from typing import List

from battle.project import Category
from battle.project import Document
from battle.project import Topic


class Storage:
    def __init__(self):
        self.categories: List = []
        self.topics: List = []
        self.documents: List = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __find_object(object_id, collection):
        result = next((r for r in collection if object_id == r.id), None)
        return result

    def edit_category(self, category_id: int, new_name: str) -> None:
        category_name = self.__find_object(category_id, self.categories)
        if category_name:
            category_name.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_object(topic_id, self.topics)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_object(document_id, self.documents)
        if document:
            document.edit(new_file_name)
    def delete_category(self, category_id):
        category = self.__find_object(category_id, self.categories)
        if category in self.categories:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_object(topic_id, self.topics)
        if topic in self.topics:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_object(document_id, self.documents)
        if document in self.documents:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__find_object(document_id, self.documents)
        return document

    def __repr__(self):
        documents = [str(d) for d in self.documents]
        return "".join(documents)
