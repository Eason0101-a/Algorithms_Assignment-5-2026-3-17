# 圖與二元搜尋樹的實作與走訪演算法分析：基於 Python 的物件導向設計

Implementation and Traversal Algorithm Analysis of Graph and BST

## 題目目標

以 Python 實作以下兩種常見資料結構與核心演算法：

1. 圖（Graph）：DFS、BFS、最短路徑（無權圖）
2. 樹（Binary Search Tree, BST）：插入、查找、四種走訪、高度計算

同時說明核心流程與時間複雜度，作為資料結構與演算法整合作業。

## 我設計的資料結構

本作業包含兩個主要類別：

### 1. Graph（鄰接串列）

- `graph`：`defaultdict(list)`，儲存每個頂點對應的鄰接頂點。
- `add_vertex(vertex)`：新增頂點。
- `add_edge(u, v, directed=True)`：新增邊（有向/無向）。
- `vertices()`：取得所有頂點。
- `edges()`：取得所有邊。
- `dfs(start_vertex)`：深度優先搜尋。
- `bfs(start_vertex)`：廣度優先搜尋。
- `shortest_path(start_vertex, target_vertex)`：以 BFS 取得無權圖最短路徑。

### 2. BinarySearchTree（BST）

- `insert(value)`：插入節點。
- `build_from_list(values)`：由列表建立 BST。
- `search(target)`：查找節點是否存在。
- `inorder_traversal()`：中序走訪。
- `preorder_traversal()`：前序走訪。
- `postorder_traversal()`：後序走訪。
- `level_order_traversal()`：層序走訪（BFS）。
- `height()`：計算樹高。

## 操作流程（高階）

1. 建立 `Graph` 物件並新增範例邊。
2. 執行 `dfs(2)` 與 `bfs(2)` 比較走訪序列。
3. 呼叫 `shortest_path(2, 1)` 取得最短路徑。
4. 建立 `BinarySearchTree` 並插入測試資料。
5. 執行 BST 的查找、四種走訪與樹高計算。
6. 輸出兩組結構的結果，觀察差異。

## 時間複雜度分析

令圖的頂點數為 $V$、邊數為 $E$；樹的節點數為 $n$，樹高為 $h$。

### 1) 新增邊 `add_edge(u, v)`

- 時間：$O(1)$（平均）
- 空間：$O(1)$（每次新增一條邊）

### 2) DFS（深度優先搜尋）

- 時間：$O(V + E)$
- 空間：$O(V)$（`visited` 集合與遞迴堆疊）

### 3) BFS（廣度優先搜尋）

- 時間：$O(V + E)$
- 空間：$O(V)$（`visited` 集合與佇列）

### 4) 最短路徑 `shortest_path()`（無權圖）

- 時間：$O(V + E)$
- 空間：$O(V)$（`visited`、`parent`、佇列）

### 5) BST 插入 / 查找

- 平均：$O(\log n)$
- 最壞（退化鏈狀）：$O(n)$
- 空間：$O(1)$（迭代版本）

### 6) BST 各種走訪

- `inorder_traversal()`：時間 $O(n)$，空間 $O(h)$
- `preorder_traversal()`：時間 $O(n)$，空間 $O(h)$
- `postorder_traversal()`：時間 $O(n)$，空間 $O(h)$
- `level_order_traversal()`：時間 $O(n)$，空間 $O(w)$（$w$ 為最大寬度）

### 7) BST 高度 `height()`

- 時間：$O(n)$
- 空間：$O(h)$

### 綜合複雜度

| 方法 | 時間複雜度 | 空間複雜度 | 說明 |
| --- | --- | --- | --- |
| `add_edge` | $O(1)$ | $O(1)$ | 鄰接串列尾端插入 |
| `dfs` | $O(V+E)$ | $O(V)$ | 每個頂點與邊最多處理一次 |
| `bfs` | $O(V+E)$ | $O(V)$ | 佇列逐層展開走訪 |
| `shortest_path` | $O(V+E)$ | $O(V)$ | BFS + parent 回溯 |
| `insert/search` (BST) | 平均 $O(\log n)$ / 最壞 $O(n)$ | $O(1)$ | 迭代沿路徑操作 |
| `tree traversals` (BST) | $O(n)$ | $O(h)$ 或 $O(w)$ | DFS/BFS 走訪整棵樹 |
| `height` (BST) | $O(n)$ | $O(h)$ | 遞迴計算高度 |

## 程式檔案

1. `graph_traversal.py` - Graph 與 BinarySearchTree 完整實作與示範

可直接執行：

```bash
python graph_traversal.py
```

## 實測結果（範例輸出）

執行後輸出如下：

```text
==============================================================
作業 5：圖與樹走訪（DFS vs BFS）
時間複雜度：O(V + E)
==============================================================

				[A]
			 /   \
		 [B]   [C]
		/ \    / \
	[D] [E] [F] [G]

--- 1. 深度優先搜尋（DFS）- 使用堆疊 ---
走訪路徑：A B D E C F G
[耗時 (O(V+E))：xxxx ns]

--- 2. 廣度優先搜尋（BFS）- 使用佇列 ---
走訪路徑：A B C D E F G
[耗時 (O(V+E))：xxxx ns]

==============================================================
進階示範：Graph + 二元搜尋樹
==============================================================

[圖結構功能]
DFS（遞迴）起點 2：[2, 0, 1, 3]
DFS（堆疊）起點 2：[2, 0, 1, 3]
BFS 起點 2：[2, 0, 3, 1]
頂點：[0, 1, 2, 3]
邊：[(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
從 2 到 1 的最短路徑：[2, 0, 1]

[BST 樹結構功能]
查找 12：True
查找 99：False
中序：[2, 5, 7, 10, 12, 15, 20]
前序：[10, 5, 2, 7, 15, 12, 20]
後序：[2, 7, 5, 12, 20, 15, 10]
層序：[10, 5, 15, 2, 7, 12, 20]
樹高：2
```

## 結論

本作業完整整合了圖與樹兩種經典資料結構：

- 在圖中，DFS 與 BFS 展示不同的探索策略，並可進一步求無權最短路徑。
- 在 BST 中，透過中序、前序、後序、層序走訪可觀察不同訪問順序。

整體程式具備良好可讀性與擴充性，可作為後續進階主題（加權最短路徑、平衡樹、圖的連通分量分析）的基礎版本。