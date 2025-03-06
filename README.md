## Bioland Grafana Template  
此页面为 Bioland Grafana 监控定制化模板。  

使用到的 Data sources 主要为 Prometheus，SLURM 页面使用 Infinity 结合 Plotly panel 绘制直方图与气泡图。  

在节点较多时，一段时间后某些 panel 由于计算表达式数据刷新会变慢，因此配置了一些rules，见 recording_rules.yml  

其中用到的 exporter 包括：

- **CPU 节点**：`node_exporter`
- **GPU 节点**：`node_exporter`、`nvidia_gpu_prometheus_exporter`
- **Slurm 主节点（192.168.1.42）**：`slurm_exporter.py`  

由于在展示时部分数据区分了 CPU 节点与 GPU 节点，因此在 CPU 节点上 node_exporter 使用 9200 端口，在 GPU 节点上 node_exporter 使用9100端口。  