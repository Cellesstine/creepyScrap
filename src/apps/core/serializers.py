from rest_framework import serializers


class NetworkSerializer(serializers.Serializer):
	accessPoint = serializers.CharField(max_length=25, required=True)

	def validate_accessPoint(self, value):
		if not(value.startswith("fh_")):
			raise serializers.ValidationError("fiberHome <unkownPattern>")

		return value.lower().removesuffix("_5g")
