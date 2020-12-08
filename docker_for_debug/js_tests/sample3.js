const { Builder, By, Key, until } = require('selenium-webdriver');
const { expect } = require('chai');

var driver = new Builder()
.withCapabilities({'browserName': 'chrome','name':'Chrome Test','tz':'America/Los_Angeles','build':'Chrome Build','idleTimeout':'60'})
.usingServer('http://selenium_hub:4444/wd/hub')
.build();

describe('DefaultTest', function () {
    this.timeout(15000);
    it('should go to nehalist.io and check the title', async () => {
        await driver.get('https://www.google.com');
        await driver.sleep(20000);
        await driver.findElement(By.name('q')).sendKeys('nehalist', Key.ENTER);
        await driver.wait(until.elementLocated(By.id('search')));
        await driver.findElement(By.linkText('nehalist.io')).click();
        const title = await driver.getTitle();

        expect(title).to.equal('nehalist.io');
    });

    after(async () => driver.quit());
});