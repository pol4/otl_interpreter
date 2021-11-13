import datetime
from rest_framework import serializers


class TimestampField(serializers.Field):

    def to_internal_value(self, data):
        """
        Transform the *incoming* primitive data into a native value.
        """
        return datetime.datetime.fromtimestamp(int(data))

    def to_representation(self, value):
        """
        Transform the *outgoing* native value into primitive data.
        """
        return int(value.timestamp())


class MakeJobSerislizer(serializers.Serializer):
    otl_query = serializers.CharField()
    tws = TimestampField()
    twf = TimestampField()
    cache_ttl = serializers.IntegerField(min_value=0, default=None, allow_null=True)
    timeout = serializers.IntegerField(min_value=0, default=None, allow_null=True)
    shared_post_processing = serializers.BooleanField(default=None, allow_null=True)
    subsearch_is_node_job = serializers.BooleanField(default=None, allow_null=True)

