import { writable } from 'svelte/store';
export const graphData = writable({ nodes: [], edges: [] });
export const showGraphPanel = writable(true);
