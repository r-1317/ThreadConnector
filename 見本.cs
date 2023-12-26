string DatToHtml(string datSouce) {
    StringBuilder htmlText = new StringBuilder("<HTML>");
    string[] datElements = datSouce.Split(new string[] { "<>" }, StringSplitOptions.None);
    int res = 1;

    htmlText.Append("<H2>" + datElements[4].Split(new char[] { '\n' })[0] + "</H2>");

    htmlText.Append(res.ToString() + ": " + "NAME:" + datElements[0] + "[" + datElements[1] + "] DATE:" + datElements[2] + "<br><br>" + datElements[3] + "<br>");
    res++;
    for(int i = 4; i < datElements.Length - 4; i = i + 4) {
        htmlText.Append("<hr>");
        htmlText.Append(res.ToString() + ": " + "NAME:" + (i == 4 ? datElements[i].Split(new char[] { '\n' })[1] : datElements[i]) + "[" + datElements[i + 1] + "] DATE:" + datElements[i + 2] + "<br><br>" + datElements[i + 3] + "<br>");
        res++;
    }
    htmlText.Replace("<b>", "");
    htmlText.Replace("</b>", "");
    return htmlText.ToString();
}