"""
Test script to verify S3 upload permissions
"""
import boto3
from botocore.exceptions import ClientError
import os
from pathlib import Path

# تفاصيل الـ S3 من settings
AWS_ACCESS_KEY_ID = 'AKIATLZTET6BNTERQSPL'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'recipes-app-bucket-nti'
AWS_S3_REGION_NAME = 'us-east-1'

def test_s3_connection():
    """Test S3 connection and permissions"""
    try:
        # إنشاء S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME
        )
        
        print("✅ S3 Client created successfully")
        
        # محاولة list الـ bucket
        response = s3_client.list_objects_v2(
            Bucket=AWS_STORAGE_BUCKET_NAME,
            MaxKeys=5
        )
        
        print(f"✅ Successfully listed bucket contents")
        print(f"   Bucket: {AWS_STORAGE_BUCKET_NAME}")
        
        if 'Contents' in response:
            print(f"   Files found: {len(response['Contents'])}")
            for obj in response['Contents'][:5]:
                print(f"   - {obj['Key']}")
        else:
            print("   No files found in bucket")
        
        # محاولة رفع ملف test
        test_content = b"Test file from Django app"
        test_key = "media/test_upload.txt"
        
        s3_client.put_object(
            Bucket=AWS_STORAGE_BUCKET_NAME,
            Key=test_key,
            Body=test_content
            # ACL removed - using bucket policy instead
        )
        
        print(f"\n✅ Successfully uploaded test file!")
        print(f"   URL: https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{test_key}")
        
        # محاولة حذف الملف
        s3_client.delete_object(
            Bucket=AWS_STORAGE_BUCKET_NAME,
            Key=test_key
        )
        print(f"✅ Successfully deleted test file")
        
        print("\n" + "="*50)
        print("🎉 All S3 permissions are working correctly!")
        print("="*50)
        return True
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_msg = e.response['Error']['Message']
        print(f"\n❌ Error: {error_code}")
        print(f"   Message: {error_msg}")
        
        if error_code == 'AccessDenied':
            print("\n⚠️  IAM User doesn't have sufficient permissions!")
            print("   Required permissions:")
            print("   - s3:ListBucket")
            print("   - s3:PutObject")
            print("   - s3:PutObjectAcl")
            print("   - s3:GetObject")
            print("   - s3:DeleteObject")
        
        return False
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        return False

if __name__ == '__main__':
    print("Testing S3 Upload Permissions...")
    print("="*50)
    test_s3_connection()
