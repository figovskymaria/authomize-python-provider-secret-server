from base_provider import ApplicationConfiguration, AuthomizeApiConfiguration
from secret__server_provider.configuration.client_configuration import OneloginClientConfiguration
from secret__server_provider.configuration.shared_configuration import OneloginSharedConfiguration
from secret__server_provider.workflows.health_checker import OneloginHealthChecker
from secret__server_provider.workflows.runner import OneloginRunner


def example():
    authomize_api_configuration = AuthomizeApiConfiguration(
        auth_token='123',
        api_url='https://api.authomize.com',
    )
    client_configuration = OneloginClientConfiguration(
        base_url='https://data.authomize.com',
        domain='mycompany',
        token='123',
    )
    application_configuration = ApplicationConfiguration(
        app_id='1234',
    )
    shared_configuration = OneloginSharedConfiguration()
    health_checker = OneloginHealthChecker(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
    )
    workflow_run = OneloginRunner(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
        application_configuration=application_configuration,
        shared_configuration=shared_configuration,
    )
    health_checker.raise_unhealthy()
    workflow_run.run()
