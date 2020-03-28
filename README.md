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

![Screen Shot 2020-03-27 at 11.12.16 PM](img/Screen%20Shot%202020-03-27%20at%2011.12.16%20PM.png)

Wait for a while

```
kubectl get pods
```

![Screen Shot 2020-03-27 at 11.12.45 PM](img/Screen%20Shot%202020-03-27%20at%2011.12.45%20PM.png)

We see the "2/2" and "1/2", which means that the sidecars have been injected so that there are 2 containers in each pod.

```bash
kubectl logs redis-client-bc84977c9-nqxr7 redis-client
```

See the successful connection with redis. Since the app hasn't been implemented, so, there is failures after the execution of the client.py.

![Screen Shot 2020-03-27 at 11.13.33 PM](img/Screen%20Shot%202020-03-27%20at%2011.13.33%20PM.png)

```bash
kubectl logs redis-client-bc84977c9-nqxr7 istio-proxy
```

![Screen Shot 2020-03-27 at 11.13.57 PM](img/Screen%20Shot%202020-03-27%20at%2011.13.57%20PM.png)

```bash
kubectl logs redis-74c769c975-fqnzw redis
```

![Screen Shot 2020-03-27 at 11.15.23 PM](img/Screen%20Shot%202020-03-27%20at%2011.15.23%20PM.png)

```bash
kubectl logs redis-74c769c975-fqnzw istio-proxy
```

![Screen Shot 2020-03-27 at 11.15.40 PM](img/Screen%20Shot%202020-03-27%20at%2011.15.40%20PM.png)

```bash
kubectl logs redis-test-665489f9b5-lt8f2 redis-test
```

![Screen Shot 2020-03-27 at 11.16.59 PM](img/Screen%20Shot%202020-03-27%20at%2011.16.59%20PM.png)

```bash
kubectl logs redis-test-665489f9b5-lt8f2 istio-proxy
```

![Screen Shot 2020-03-27 at 11.17.26 PM](img/Screen%20Shot%202020-03-27%20at%2011.17.26%20PM.png)



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
cd istio-redis-test-set/redis/client/python-docs-samples/memorystore/redis
sudo docker build -t tiancanyu/redis-client:v1 .; sudo docker push tiancanyu/redis-client:v1
```

