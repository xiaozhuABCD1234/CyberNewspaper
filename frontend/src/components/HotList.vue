<!-- components/HotList.vue -->
<template>
  <div class="hotlist-card">
    <h2>{{ title }}</h2>

    <div v-if="loading" class="loading">加载中...</div>
    <div v-if="error" class="error">{{ error }}</div>

    <div v-else class="list-container">
      <div v-for="(item, index) in listData" :key="item.url" class="list-item">
        <div class="rank">{{ index + 1 }}</div>

        <img v-if="config.fields.image && item.image" :src="item.image" class="cover" @error="handleImageError">

        <div class="content">
          <a :href="item.url" target="_blank" class="title">
            {{ item.title }}
          </a>

          <div class="meta">
            <span class="heat">
              {{ config.heatLabel }}: {{ formatHeat(item.heat) }}
            </span>
          </div>

          <div v-if="config.fields.description && item.description" class="description">
            {{ truncateDescription(item.description) }}
          </div>

          <div v-if="config.fields.author && item.author" class="author">
            作者: {{ item.author }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, onBeforeUnmount } from 'vue'
import { ref, watch, onMounted } from 'vue'
import axios from 'axios'

const props = defineProps({
  title: String,
  config: {
    type: Object,
    required: true,
    validator: (value) => {
      return 'apiUrl' in value && 'heatLabel' in value
    }
  }
})

const listData = ref([])
const loading = ref(false)
const error = ref(null)

// 获取数据
const fetchData = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await axios.get(props.config.apiUrl)
    listData.value = response.data
  } catch (err) {
    error.value = `数据加载失败: ${err.message}`
    console.error('API请求错误:', err)
  } finally {
    loading.value = false
  }
}

// 自动刷新数据
const autoRefresh = () => {
  fetchData()
  const timer = setInterval(fetchData, 300000) // 5分钟刷新一次
  onBeforeUnmount(() => clearInterval(timer))
}

// 格式化热度值
const formatHeat = (value) => {
  if (typeof value === 'number') {
    return value >= 10000 ? `${(value / 10000).toFixed(1)}万` : value
  }
  return value
}

// 截断长描述
const truncateDescription = (text) => {
  return text.length > 100 ? text.slice(0, 100) + '...' : text
}

// 图片加载失败处理
const handleImageError = (e) => {
  e.target.style.display = 'none'
}

// 初始化获取数据
onMounted(() => {
  fetchData()
  autoRefresh()
})

// 监听配置变化
watch(() => props.config.apiUrl, () => {
  fetchData()
})
</script>

<style scoped>
.hotlist-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
  padding: 20px;
}

h2 {
  color: #1a1a1a;
  font-size: 1.5rem;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 2px solid #f0f0f0;
}

.list-item {
  display: flex;
  align-items: flex-start;
  padding: 16px;
  margin-bottom: 12px;
  background: #f8f9fa;
  border-radius: 8px;
  transition: transform 0.2s;
}

.list-item:hover {
  transform: translateX(5px);
}

.rank {
  font-size: 18px;
  font-weight: bold;
  color: #666;
  min-width: 40px;
  text-align: center;
  margin-right: 15px;
}

.cover {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 4px;
  margin-right: 20px;
}

.content {
  flex: 1;
}

.title {
  font-size: 16px;
  font-weight: 500;
  color: #1a0dab;
  text-decoration: none;
  display: block;
  margin-bottom: 8px;
}

.title:hover {
  text-decoration: underline;
}

.meta {
  margin: 8px 0;
  font-size: 14px;
}

.heat {
  color: #ff5722;
  margin-right: 15px;
}

.description {
  color: #666;
  line-height: 1.6;
  margin: 8px 0;
}

.author {
  color: #666;
  font-size: 0.9em;
}

.loading,
.error {
  padding: 20px;
  text-align: center;
  color: #666;
}

.error {
  color: #ff4444;
}

@media (max-width: 768px) {
  .list-item {
    flex-direction: column;
  }

  .cover {
    width: 100%;
    height: auto;
    margin-bottom: 10px;
  }
}
</style>
