# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.extensions_v1beta1_api import ExtensionsV1beta1Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestExtensionsV1beta1Api(unittest.TestCase):
    """ExtensionsV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.extensions_v1beta1_api.ExtensionsV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_daemon_set(self):
        """Test case for create_namespaced_daemon_set

        """
        pass

    def test_create_namespaced_deployment(self):
        """Test case for create_namespaced_deployment

        """
        pass

    def test_create_namespaced_deployment_rollback(self):
        """Test case for create_namespaced_deployment_rollback

        """
        pass

    def test_create_namespaced_ingress(self):
        """Test case for create_namespaced_ingress

        """
        pass

    def test_create_namespaced_network_policy(self):
        """Test case for create_namespaced_network_policy

        """
        pass

    def test_create_namespaced_replica_set(self):
        """Test case for create_namespaced_replica_set

        """
        pass

    def test_create_pod_security_policy(self):
        """Test case for create_pod_security_policy

        """
        pass

    def test_delete_collection_namespaced_daemon_set(self):
        """Test case for delete_collection_namespaced_daemon_set

        """
        pass

    def test_delete_collection_namespaced_deployment(self):
        """Test case for delete_collection_namespaced_deployment

        """
        pass

    def test_delete_collection_namespaced_ingress(self):
        """Test case for delete_collection_namespaced_ingress

        """
        pass

    def test_delete_collection_namespaced_network_policy(self):
        """Test case for delete_collection_namespaced_network_policy

        """
        pass

    def test_delete_collection_namespaced_replica_set(self):
        """Test case for delete_collection_namespaced_replica_set

        """
        pass

    def test_delete_collection_pod_security_policy(self):
        """Test case for delete_collection_pod_security_policy

        """
        pass

    def test_delete_namespaced_daemon_set(self):
        """Test case for delete_namespaced_daemon_set

        """
        pass

    def test_delete_namespaced_deployment(self):
        """Test case for delete_namespaced_deployment

        """
        pass

    def test_delete_namespaced_ingress(self):
        """Test case for delete_namespaced_ingress

        """
        pass

    def test_delete_namespaced_network_policy(self):
        """Test case for delete_namespaced_network_policy

        """
        pass

    def test_delete_namespaced_replica_set(self):
        """Test case for delete_namespaced_replica_set

        """
        pass

    def test_delete_pod_security_policy(self):
        """Test case for delete_pod_security_policy

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_daemon_set_for_all_namespaces(self):
        """Test case for list_daemon_set_for_all_namespaces

        """
        pass

    def test_list_deployment_for_all_namespaces(self):
        """Test case for list_deployment_for_all_namespaces

        """
        pass

    def test_list_ingress_for_all_namespaces(self):
        """Test case for list_ingress_for_all_namespaces

        """
        pass

    def test_list_namespaced_daemon_set(self):
        """Test case for list_namespaced_daemon_set

        """
        pass

    def test_list_namespaced_deployment(self):
        """Test case for list_namespaced_deployment

        """
        pass

    def test_list_namespaced_ingress(self):
        """Test case for list_namespaced_ingress

        """
        pass

    def test_list_namespaced_network_policy(self):
        """Test case for list_namespaced_network_policy

        """
        pass

    def test_list_namespaced_replica_set(self):
        """Test case for list_namespaced_replica_set

        """
        pass

    def test_list_network_policy_for_all_namespaces(self):
        """Test case for list_network_policy_for_all_namespaces

        """
        pass

    def test_list_pod_security_policy(self):
        """Test case for list_pod_security_policy

        """
        pass

    def test_list_replica_set_for_all_namespaces(self):
        """Test case for list_replica_set_for_all_namespaces

        """
        pass

    def test_patch_namespaced_daemon_set(self):
        """Test case for patch_namespaced_daemon_set

        """
        pass

    def test_patch_namespaced_daemon_set_status(self):
        """Test case for patch_namespaced_daemon_set_status

        """
        pass

    def test_patch_namespaced_deployment(self):
        """Test case for patch_namespaced_deployment

        """
        pass

    def test_patch_namespaced_deployment_scale(self):
        """Test case for patch_namespaced_deployment_scale

        """
        pass

    def test_patch_namespaced_deployment_status(self):
        """Test case for patch_namespaced_deployment_status

        """
        pass

    def test_patch_namespaced_ingress(self):
        """Test case for patch_namespaced_ingress

        """
        pass

    def test_patch_namespaced_ingress_status(self):
        """Test case for patch_namespaced_ingress_status

        """
        pass

    def test_patch_namespaced_network_policy(self):
        """Test case for patch_namespaced_network_policy

        """
        pass

    def test_patch_namespaced_replica_set(self):
        """Test case for patch_namespaced_replica_set

        """
        pass

    def test_patch_namespaced_replica_set_scale(self):
        """Test case for patch_namespaced_replica_set_scale

        """
        pass

    def test_patch_namespaced_replica_set_status(self):
        """Test case for patch_namespaced_replica_set_status

        """
        pass

    def test_patch_namespaced_replication_controller_dummy_scale(self):
        """Test case for patch_namespaced_replication_controller_dummy_scale

        """
        pass

    def test_patch_pod_security_policy(self):
        """Test case for patch_pod_security_policy

        """
        pass

    def test_read_namespaced_daemon_set(self):
        """Test case for read_namespaced_daemon_set

        """
        pass

    def test_read_namespaced_daemon_set_status(self):
        """Test case for read_namespaced_daemon_set_status

        """
        pass

    def test_read_namespaced_deployment(self):
        """Test case for read_namespaced_deployment

        """
        pass

    def test_read_namespaced_deployment_scale(self):
        """Test case for read_namespaced_deployment_scale

        """
        pass

    def test_read_namespaced_deployment_status(self):
        """Test case for read_namespaced_deployment_status

        """
        pass

    def test_read_namespaced_ingress(self):
        """Test case for read_namespaced_ingress

        """
        pass

    def test_read_namespaced_ingress_status(self):
        """Test case for read_namespaced_ingress_status

        """
        pass

    def test_read_namespaced_network_policy(self):
        """Test case for read_namespaced_network_policy

        """
        pass

    def test_read_namespaced_replica_set(self):
        """Test case for read_namespaced_replica_set

        """
        pass

    def test_read_namespaced_replica_set_scale(self):
        """Test case for read_namespaced_replica_set_scale

        """
        pass

    def test_read_namespaced_replica_set_status(self):
        """Test case for read_namespaced_replica_set_status

        """
        pass

    def test_read_namespaced_replication_controller_dummy_scale(self):
        """Test case for read_namespaced_replication_controller_dummy_scale

        """
        pass

    def test_read_pod_security_policy(self):
        """Test case for read_pod_security_policy

        """
        pass

    def test_replace_namespaced_daemon_set(self):
        """Test case for replace_namespaced_daemon_set

        """
        pass

    def test_replace_namespaced_daemon_set_status(self):
        """Test case for replace_namespaced_daemon_set_status

        """
        pass

    def test_replace_namespaced_deployment(self):
        """Test case for replace_namespaced_deployment

        """
        pass

    def test_replace_namespaced_deployment_scale(self):
        """Test case for replace_namespaced_deployment_scale

        """
        pass

    def test_replace_namespaced_deployment_status(self):
        """Test case for replace_namespaced_deployment_status

        """
        pass

    def test_replace_namespaced_ingress(self):
        """Test case for replace_namespaced_ingress

        """
        pass

    def test_replace_namespaced_ingress_status(self):
        """Test case for replace_namespaced_ingress_status

        """
        pass

    def test_replace_namespaced_network_policy(self):
        """Test case for replace_namespaced_network_policy

        """
        pass

    def test_replace_namespaced_replica_set(self):
        """Test case for replace_namespaced_replica_set

        """
        pass

    def test_replace_namespaced_replica_set_scale(self):
        """Test case for replace_namespaced_replica_set_scale

        """
        pass

    def test_replace_namespaced_replica_set_status(self):
        """Test case for replace_namespaced_replica_set_status

        """
        pass

    def test_replace_namespaced_replication_controller_dummy_scale(self):
        """Test case for replace_namespaced_replication_controller_dummy_scale

        """
        pass

    def test_replace_pod_security_policy(self):
        """Test case for replace_pod_security_policy

        """
        pass


if __name__ == '__main__':
    unittest.main()