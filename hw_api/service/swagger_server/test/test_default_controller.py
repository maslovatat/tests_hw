# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.new_task import NewTask  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.models.update_task import UpdateTask  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_tasks_get(self):
        """Test case for tasks_get

        Получить список всех заданий
        """
        response = self.client.open(
            '/api/tasks',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tasks_id_delete(self):
        """Test case for tasks_id_delete

        Удалить задание
        """
        response = self.client.open(
            '/api/tasks/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tasks_id_get(self):
        """Test case for tasks_id_get

        Получить задание по ID
        """
        response = self.client.open(
            '/api/tasks/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tasks_id_patch(self):
        """Test case for tasks_id_patch

        Обновить статус задания (например, отметить выполненным)
        """
        body = UpdateTask()
        response = self.client.open(
            '/api/tasks/{id}'.format(id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tasks_post(self):
        """Test case for tasks_post

        Создать новое задание (дедлайн)
        """
        body = NewTask()
        response = self.client.open(
            '/api/tasks',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
