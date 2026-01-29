import os
from imagekitio import ImageKit

imagekit = ImageKit(
    os.getenv("IMAGEKIT_PRIVATE_KEY"),
    os.getenv("IMAGEKIT_PUBLIC_KEY"),
    os.getenv("IMAGEKIT_URL_ENDPOINT"),
)

try:
    result = imagekit.get_account_details()
    print("✅ ImageKit credentials are VALID")
    print(result)
except Exception as e:
    print("❌ ImageKit credentials FAILED")
    print(type(e).__name__, e)
