This is a demo application created using python and flask and deployable on local docker using docker-compose and on Kubernetes using helm chart.

The application listen on port 9000 for docker-compose ie. http://localhost:9000

For Kubernetes deployment, application can be reached on public ip of load balancer ie. http://public-ip-load-balancer/

The health check is configured on /healthz route.

Prerequisites for Kubernetes deployment
    1. helm 3 installed
    
    2. kubectl installed
    
    3. metrics-server installed (Installtion steps provided below)
    
    4. nginx ingress controller installed (Installtion steps provided below)

Metrics server Installation
    1. kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    
    2. Edit the deployment using "kubectl edit deploy -n kube-system metrics-server"
    
    3. Add the below flags in arguments
    
    args:
       - --kubelet-insecure-tls
       - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname

Ingress controller Installation
    1. NAMESPACE=ingress-basic
    2. helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
    
    3. helm repo update
    
    4. helm install ingress-nginx ingress-nginx/ingress-nginx --create-namespace --namespace $NAMESPACE


Steps to deploy on Kubernetes
    1. unzip the zipped source code folder
    
    2. from the root, run ./deploy-chart.sh
    
    3. This should deploy the chart.
    
    4. After the chart is deployed, do <kubectl get pods> and search and grab the id of mysql database pod. Helm hooks can be used to populate database but for sake of simplicity, have kept it manual.
    
    5. kubectl exec -it <mysql database pod id> /bin/sh
    
    6. mysql -u root -p
    
    7. Provide <changeit> as password
    
    8. CREATE TABLE alf.test_table (PersonID varchar(255),LastName varchar(255), FirstName varchar(255));
    
       INSERT INTO alf.test_table VALUES ('1','surname1','name1');
       
       INSERT INTO alf.test_table VALUES ('2','surname2','name2');
       
    9. The above sql populates the database.
    
    10. After this, grab the public ip of the ingress-controller from the command kubectl get ingress
    
    11. Application is reachable on http://public-ip-copied-above/

Steps to deploy using docker-compose
    1. unzip the zipped source code folder
    2. from the root, run ./docker-compose.sh
    3. This will make the application up and running with 2 records present in database
    4. The application is reachable on http://localhost:9000/
