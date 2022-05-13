import aws_cdk as core
import aws_cdk.assertions as assertions

from templates.templates_stack import TemplatesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in templates/templates_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TemplatesStack(app, "templates")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
