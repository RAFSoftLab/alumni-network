from rest_framework import serializers

class GetAlumniUsersValidator(serializers.Serializer):
    company = serializers.IntegerField(required=False)

class GetAcademicHistoryValidator(serializers.Serializer):
    alumni_user = serializers.IntegerField(required=True)

class GetEmploymentHistoryValidator(serializers.Serializer):
    alumni_user = serializers.IntegerField(required=True)