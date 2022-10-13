from rest_framework import serializers

from project_management.models import Project, ProjectTool
from tools.serializers import ToolSerializer


class ProjectToolCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProjectTool
        fields = ('quantity','tool')


class ProjectToolSerializer(serializers.ModelSerializer):
    tool = ToolSerializer(read_only=True)

    class Meta:
        model=ProjectTool
        fields = ('tool', 'quantity')


class ProjectSerializer(serializers.ModelSerializer):
    tools = serializers.ListSerializer(min_length=1,child=ProjectToolCreateSerializer(),required=True,write_only=True,error_messages={'required':'tools are required'})
    schedule = serializers.IntegerField(required=False,error_messages={'required':'schedule is required'})
    project_tools=serializers.SerializerMethodField()
    # owner = UserDetailSerializer(read_only=True)

    def get_project_tools(self,obj):
        return ProjectToolSerializer(ProjectTool.objects.filter(project_id=obj.id),many=True).data

    def create(self, validated_data):
        new_project = Project.objects.create(owner_id=validated_data['owner'].id,name=validated_data['name'])
        for tool in validated_data['tools']:
            project_tool = ProjectTool.objects.create(tool_id=tool['tool'].id,project_id=new_project.id,quantity=tool['quantity'])



        return new_project

    class Meta:
        model=Project
        fields = ('id', 'owner', 'description', 'name', 'tools','schedule','project_tools')