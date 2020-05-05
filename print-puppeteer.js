// node print-puppeteer.js 
// node -v -> v14.1.0


const puppeteer = require('puppeteer');
const fs = require('fs-extra');
 
(async function printPDF() {
  try {
    const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox'], executablePath: "/snap/bin/chromium", headless: true});
    const page = await browser.newPage();
    const html = await fs.readFile('devis_dev_site.html', 'utf-8')
    console.log(html)
    await page.setContent(html)
    await page.addStyleTag({path:'templates/devis.css'})
    const pdf = await page.pdf({ 
      path: 'out_puppeteer.pdf',
      format: 'A4',
      displayHeaderFooter: true,
      headerTemplate: '<style>#pageHeader { margin: 20px; }</style><div class="text" id="pageHeader">Devis n° 12 - 30/04/2020</div>',
      footerTemplate: '<div class="text center"><span class="pageNumber"></span></div>',
    });
   
    console.log('done')
    await browser.close();
  } catch (e) {
    console.log('Erreur:',e);
  }
})();