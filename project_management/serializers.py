from rest_framework import serializers

from project_management.models import Project, ProjectTool
from schedules.serializers import ScheduleSerializer
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
    schedule_id = serializers.IntegerField(required=True,write_only=True,error_messages={'required':'schedule is required'})
    schedule = ScheduleSerializer(read_only=True)
    project_tools=serializers.SerializerMethodField()
    name = serializers.CharField()

    # owner = UserDetailSerializer(read_only=True)

    def get_project_tools(self,obj):
        return ProjectToolSerializer(ProjectTool.objects.filter(project_id=obj.id),many=True).data

    def create(self, validated_data):
        new_project = Project.objects.create(
            owner_id=validated_data['owner'].id,
            name=validated_data['name'],
            schedule_id=validated_data['schedule_id'],
            extra_instruction=validated_data['extra_instruction']
        )

        for tool in validated_data['tools']:
            project_tool = ProjectTool.objects.create(
                tool_id=tool['tool'].id,
                project_id=new_project.id,
                quantity=tool['quantity']
            )

        return new_project

    class Meta:
        model=Project
        fields = ('id', 'owner', 'description', 'name','status','schedule_id','tools','schedule','project_tools','extra_instruction')