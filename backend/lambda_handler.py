from mangum import Mangum # type: ignore
from server import app

# Create the Lambda handler
handler = Mangum(app)