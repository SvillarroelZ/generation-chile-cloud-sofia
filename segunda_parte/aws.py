import boto3
import json

# aqui se crea el cliente de ec2
# ec2=boto3.client('ec2') ##Constructores: igual que un metodo tradicional pero ayuda a instanciar objetos de un tipo en particular

ec2 = boto3.client('ec2')  # Crear el recurso de EC2
lab_instances = ec2.describe_instances()
#print(lab_instances)
#print(json.dumps(lab_instances, indent=2, sort_keys=True, default=str)) #sort_keys ordena las llaves y default=str convierte a string los objetos no serializables
instance_id = lab_instances["Reservations"][0]["Instances"][0]["InstanceId"]

print(json.dumps(instance_id, indent=2, default=str))

ec2.stop_instances(InstanceIds=["i-08c98e9a98068c9c2"])