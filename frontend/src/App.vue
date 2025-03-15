<template>
  <div class="show-hot">
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
  </div>
</template>
<script lang="ts" setup>
import axios from 'axios'
import { onMounted } from 'vue'
const title = 'Hot'
const description = 'Hot is a temperature that is higher than warm.'
const fetchData = async () => {
  axios.get('http://127.0.0.1:8000/api/hotlist/zhihu')
    .then(response => {
      console.log(response.data); // 打印返回的数据
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
onMounted(() => {
  fetchData()
})
</script>
