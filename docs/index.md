---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "推理王国"
  text: "一本关于AI推理机制的开源教程"
  tagline: 从熵增到边界，追问智能的本质
  image:
    src: ReasoningKingdom.png
    alt: 推理王国
  actions:
    - theme: brand
      text: 开始阅读
      link: /preface

features:
  - title: 🧠 深度
    details: 从信息论、符号逻辑到Transformer，系统性剖析AI推理的底层机制
  - title: 🎁 免费
    details: 全部内容开源，无任何形式收费
  - title: 🌐 开源
    details: 教程源文件托管在GitHub，欢迎贡献与反馈
---
<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [
  {
    avatar: 'https://www.github.com/lizixi-0x2F.png',
    name: '李籽溪（兔狲）',
    title: '项目负责人/笔者',
    links: [
      { icon: 'github', link: 'https://github.com/lizixi-0x2F' },
    ]
  },
]
</script>


<h2 align="center">Team</h2>
<VPTeamMembers size="small" :members />
