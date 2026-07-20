<script>
  export let data;
</script>
<div class="entity-node">{data.label}</div>

<style>
  .entity-node {
    width: 110px; height: 110px; border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #a78bfa, #7c3aed);
    color: white; display: flex; align-items: center; justify-content: center;
    text-align: center; font-size: 13px; padding: 8px;
  }
</style>
