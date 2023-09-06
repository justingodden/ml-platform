# ArgoCD

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

```bash
kubectl -n argocd port-forward svc/argocd-server 8008:80
```

[http://localhost:8008](http://localhost:8008)

Advanced... Accept the Risk and Continue

admin

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d; echo
```

update password


```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: argo-apps
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: git@github.com:justingodden/mlops-made-easy-project-code.git
    targetRevision: HEAD
    path: 06-continuous-delivery/argocd
    directory:
      recurse: true
  destination:
    server: "https://kubernetes.default.svc"
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```