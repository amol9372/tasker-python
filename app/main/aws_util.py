from ssm_parameter_store import EC2ParameterStore

# get access id and secert from aws to run on local
aws_param_store = EC2ParameterStore(region_name="ap-south-1")

google_app_credentials = aws_param_store.get_parameters_with_hierarchy(
    "/applications/google/places")
