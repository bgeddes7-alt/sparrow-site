#!/bin/zsh
# Publishes Sparrow's web layer to https://sparrowmahjong.app/app/ and saves the app source to GitHub.
# Run any time the app's HTML/JS changes:  zsh ~/geddes-apps/Sparrow-AppStore/app/publish-web.sh
set -e
APP=~/geddes-apps/Sparrow-AppStore/app
SITE=~/sparrow-site
[ -d $SITE/.git ] || git clone https://github.com/bgeddes7-alt/sparrow-site.git $SITE
cd $SITE && git pull --ff-only
rm -rf site/app && mkdir -p site/app && cp -R $APP/www/. site/app/
if ! grep -q '^/app/\*' site/_headers; then
cat >> site/_headers <<'H'
/app/*
  ! Content-Security-Policy
  ! Permissions-Policy
  ! X-Frame-Options
  Cache-Control: no-cache
H
fi
mkdir -p app-src/ios
cp $APP/capacitor.config.json $APP/package.json $APP/publish-web.sh app-src/
cp $APP/ios/App/App/AppDelegate.swift $APP/ios/App/App/App.entitlements $APP/ios/App/App/Base.lproj/Main.storyboard $APP/ios/App/App/SceneDelegate.swift app-src/ios/
npx wrangler deploy
git add -A
git commit -m "Sparrow web layer at /app + app shell source" || true
git push
echo "\nLive: https://sparrowmahjong.app/app/"
