# Test Set with redis server and client under istio injection

## setup

```bash
git clone git@github.com:CS2552F-DOSA/istio-redis-test-set.git

# modify ~/.zshrc or ~/.bash_profile (if using zsh modify ~/.zshrc, if not modify ~/.bash_profile) to set up istioctl
echo "export PATH=/Users/tiancan/project/istio-redis-test-set/istio-1.5.1/bin:$PATH" >> ~/.zshrc
source ~/.zshrc

# install istio
cd istio-redis-test-set/istio-1.5.1
kubectl delete -f install/kubernetes/istio-demo.yaml # delete old incompatible configuration
istioctl manifest apply --set profile=demo
kubectl label namespace default istio-injection=enabled # set auto injection
```



## check result and istio injection

```bash
cd ../redis
docker pull tiancanyu/redis-client:v1; kubectl delete -k .; kubectl apply -k .; kubectl get pods
```



Wait for a while

```
kubectl get pods
```



We see the "2/2" and "1/2", which means that the sidecars have been injected so that there are 2 containers in each pod.



```bash
kubectl logs visit-counter-5bd898ffbc-2mvhl visit-counter
```

See the successful connection with redis. Since the app hasn't been implemented, so, there is failures after the execution of the client.py.

![Screen Shot 2020-03-27 at 10.42.48 PM](img/Screen%20Shot%202020-03-27%20at%2010.42.48%20PM.png)

```bash
kubectl logs visit-counter-5bd898ffbc-2mvhl istio-proxy
```

![Screen Shot 2020-03-27 at 10.45.04 PM](img/Screen%20Shot%202020-03-27%20at%2010.45.04%20PM.png)

```bash
kubectl logs redis-74c769c975-9bnn9 redis
```

![Screen Shot 2020-03-27 at 10.46.42 PM](img/Screen%20Shot%202020-03-27%20at%2010.46.42%20PM-5363632.png)

```bash
kubectl logs redis-74c769c975-9bnn9 istio-proxy
```

![Screen Shot 2020-03-27 at 10.47.28 PM](img/Screen%20Shot%202020-03-27%20at%2010.47.28%20PM.png)



To close the instances.

```bash
cd istio-redis-test-set/redis
kubectl delete -k .
```



## Others

The server for redis is implemented in istio-redis-test-set/redis

The test client code is implemented in istio-redis-test-set/redis/client/python-docs-samples/memorystore/redis

If the test client code has been changed, the docker file needs to be built again.

```bash
git pull
cd istio-redis-test-set/redis/client/python-docs-samples/memorystore/redis
sudo docker build -t tiancanyu/redis-client:v1 .; sudo docker push tiancanyu/redis-client:v1
```

