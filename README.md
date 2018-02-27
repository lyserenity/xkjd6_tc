星空鍵道6.0輸入方案作者：吅吅大山（大牛），該方案的教程、簡介或特點可至以下連結一探究竟:
  - [鍵道網盤][ys168]
  - [鍵道官網](https://xkjd.coding.me/)
  - [星空鍵道6簡明教程][thxnder_help]
 
> 如果真的還有疑問，也可至大牛雙拼 QQ 群 ( [320053116](https://jq.qq.com/?_wv=1027&k=5sTEYIQ) )
> 與眾多群友一同討論。

---
<br>

# :bookmark: 項目簡介
    
1. 本項目僅提供由個人維護的**碼表繁體版**，可導入其他輸入法平台使用
2. 項目所提供之碼表本質皆是純文字檔，主要以 RIME 及落格平台適用之格式為優先；其他平台請自行更改
<table style="border-top:2px  solid;border-bottom:2px solid;border-right:1px hidden;border-left:1px hidden;" cellpadding="10" border='1'>
  <colgroup>
    <col style="border-right:1px hidden">
  </colgroup>
  <tr style='border-bottom:solid 2px;'>
  　<th align="center" valign="center">輸入法</th>
  　<th align="center" valign="center" colspan=2>輸入法檔案</th>
  　<th align="center" valign="center">輸入法支持平台</th>
  <colgroup>
    <col style="border-right:1px hidden">
  </colgroup>
　<tr>
  　<td>落格</td>
    <td>單詞混合</td>
    <td>xkjd6_落格.txt</td>
    <td>mac / ios</td>
　</tr>
  <colgroup>
    <col style="border-right:1px hidden">
    </colgroup>
<tr style='border-bottom:2px hidden;'>
  　<td rowspan="3">RIME</td>
  　<td>單字</td>
  　<td>rimeDict/xkjd6_tc.danzi.dict.yaml</td>
  　<td rowspan="3">win / mac / ios / android/</td>
　</tr>
　<tr>
  　<td>詞組</td>
  　<td>rimeDict/xkjd6_tc.cizu.dict.yaml</td>
　</tr>
<tr>
  　<td>630聲筆(筆)詞組</td>
  　<td>rimeDict/xkjd6_tc.cizu.dict.yaml</td>
　</tr>
</table>

3. 繁體碼表基於鍵道規則編碼，由於繁體字形較為繁複，且未經方案作者的審核，
恐有缺字、編碼錯落或理解有誤的地方，也歡迎各位提出。

<!-- 簡體版可至以下專案下載: -->
<!--   - 多多輸入法: [吅吅大山的網盤][ys168] -->
<!--   - 小小輸入法平台: [小小鍵道][thxnder] -->
<!--   - RIME 鍵道: [同文版和 Windows 平台][Rime_JD] -->

<br>

# :memo: 繁體碼表使用須知

## 說明

#### 單字

以繁體字形為編碼，以下僅指出使用繁體版碼表中筆形碼須注意的地方：  
 
  - 「言」字、部首或以其為偏旁的字：編碼使用 `oa`
    - 考量如果使用 `ov` ，重碼可能增加
    - 可視為雙編碼形式
  - 「門」以此為部首或偏旁所構成的字：維持簡體版編碼 `oi`
  - 「東」、「車」二字及以其為偏旁的字：維持簡體版編碼 `va` 編碼
  - 「食」：筆畫取 `人` 和 `、(點)`，即為 `io`
    - 注意：「倉、今」等構成之字皆取 `io`

#### 詞組

  - 105 聲筆 (SB) 和 525 聲筆筆 (SBB)詞組
    - 該詞組群因有用字頻率上的考量，筆形碼的部分未能以繁體字編碼替換
  - 一般詞組: 目前詞組碼表僅對筆畫的部分作變動，不涉及用語等差異增減

<br>

# :ballot_box_with_check:  待處理

- add: 一對多繁體詞組

---
<!-- # 版權聲明 -->
<!--  -->
<!-- 「星空键道6.0」作者：[**吅吅大山（大牛）**](https://xkjd.coding.me/)   -->
<!-- 「RIME键道」维护者：[**倾书（Qshu）**][Rime_JD]   -->
<!-- 「小小键道」维护者：[**thXnder**](https://gitee.com/thxnder/xxjd) -->



[ys168]: http://daniushuangpin.ys168.com/
[Rime_JD]: https://gitee.com/nmlixa/Rime_JD
[thxnder]: https://gitee.com/thxnder/xxjd
[official_help]: https://xkjd.coding.me/doc/
[thxnder_help]: https://gitee.com/thxnder/xxjd/wikis/pages?title=Home
